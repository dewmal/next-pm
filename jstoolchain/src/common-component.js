import {LitElement} from "lit";

class BaseElement extends LitElement {
    constructor() {
        super();
    }
    createRenderRoot() {
        return this; // turn off shadow dom to access external styles
    }
}

export default BaseElement;