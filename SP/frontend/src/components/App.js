import React, {Component} from "react";
import { render } from "react-dom";

export default class App extends Component {
    constructor(props){
        super(props);
    }

    render(){
        return <h1>Hi boss</h1>;
    }
}

const AppDiv = document.getElementById("app")
render(<App/>, AppDiv)