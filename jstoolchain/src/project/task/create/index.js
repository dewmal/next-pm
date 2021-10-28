import {html} from 'lit'
import {classMap} from 'lit/directives/class-map.js';
import BaseElement from "common-component";
import {getTaskStatus, updateTask} from "Transport";
import moment from "moment";

const stateMap = new WeakMap();

class TaskUpdateForm extends BaseElement {

    constructor() {
        super();
        this.form = {
            description: 'tes',
            pullRequest: 'test',
            endTime: null,
            status: 'FI'
        }
        this.statusList = [];
        this.fetchData();
    }

    async fetchData() {
        this.statusList = await getTaskStatus();
    }

    async submit(e) {
        e.preventDefault();
        const form = new FormData(e.target);
        const {id, description, pullRequest, endTime, status} = Object.fromEntries(form.entries());
        const res = await updateTask({
            id,
            description,
            pullRequest,
            status,
            endTime: moment(endTime).format('YYYY-MM-DD HH:mm:ss')
        });
        const {ok, task} = res
        if (ok) {
            this.dispatchEvent(new CustomEvent('task-updated', {detail: task}));
        }
    }


    render() {
        return html`
            <div @submit="${this.submit}">
                <form method="post" class="grid gap-4 grid-cols-1  bg-gray-100 p-4 rounded-sm">
                    <input name="id" .value="${this.getAttribute("taskId")}" type="hidden">
                    <div class="grid gap-2 grid-cols-3">
                        <div class="col-span-2 flex flex-col gap-2">
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">Description</span>
                                </label>
                                <textarea placeholder="Description"
                                          .value="${this.form.description}"
                                          name="description" class="textarea h-24 textarea-bordered"">
                                </textarea>
                            </div>
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">Pull request</span>
                                </label>
                                <textarea placeholder="Pull request"
                                          .value="${this.form.pullRequest}"
                                          name="pullRequest" class="textarea h-24 textarea-bordered"">

                                </textarea>
                            </div>

                            <div class="form-control">
                                <button
                                        type="submit" class="btn btn-primary">Save
                                </button>
                            </div>
                        </div>
                        <div class="flex flex-col gap-2">
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">End time</span>
                                </label>
                                <input
                                        .value=${this.form.endTime}
                                        type="datetime-local" placeholder="End Time"
                                        name="endTime" class="input input-bordered">
                            </div>
                            <div class="form-control">
                                <label class="label">
                                    <span class="label-text">Status</span>
                                </label>
                                <select
                                        .value=${this.form.status}
                                        type="datetime-local" name="status"
                                        class="input input-bordered">
                                    ${this.statusList.map((st) => {
                                        return html`
                                            <option value="${st.value}">${st.name}</option>
                                        `;
                                    })}
                                </select>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        `;
    }
}

TaskUpdateForm.properties = {
    taskId: {type: Number},
    statusList: [],
    form: {
        description: 'tes',
        pullRequest: 'test',
        endTime: null,
        status: 'FI'
    }
}
customElements.define("tuf-task-update-form", TaskUpdateForm)

class TaskEndPanel extends BaseElement {

    constructor() {
        super()
        this.opened = false
    }

    render() {
        console.log(this.taskId);
        return html`
            <style>
                .opened {
                    display: block;
                }

                .closed {
                    display: none;
                }
            </style>
            <div class="${classMap({opened: !this.opened, closed: this.opened})}">
                <tuf-task-update-form
                        taskId="${this.getAttribute("taskId")}"></tuf-task-update-form>

            </div>`
    }
}

TaskEndPanel.properties = {
    taskId: {type: Number, attribute: true},
    opened: {type: Boolean}
}
customElements.define('ts-task-panel', TaskEndPanel)

class TaskFinishComponent extends BaseElement {
    constructor() {
        super()
        this.dialogVisible = false
    }


    render() {
        return html`
            <div class="flex flex-col gap-2">
                <div>
                    <button
                            class="btn btn-block btn-danger"
                            @click="${this.toggleDialog.bind(this)}">
                        Close Task
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
                             stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                  d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"/>
                        </svg>
                    </button>
                </div>
                <ts-task-panel
                        taskId="${this.getAttribute("taskId")}"
                        ?opened="${this.dialogVisible}"
                        @dialog.accept="${this.closeDialog.bind(this)}"
                        @dialog.cancel="${this.closeDialog.bind(this)}"></ts-task-panel>
            </div>`
    }

    toggleDialog(e) {
        this.dialogVisible = !this.dialogVisible
    }

    closeDialog(e) {
        this.dialogVisible = false
    }
}

TaskFinishComponent.properties = {
    taskId: {type: Number, attribute: true},
    dialogVisible: {type: Boolean}
}
export default TaskFinishComponent;