import  React, {Component} from 'react';
import { render } from 'react-dom';
import RoomJoinPage from "./RoomJoinPage";
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';
// import { BrowserRouter as Router, Route, Link } from "react-router-dom";


export default class HomePage extends Component {
    constructor(props){
        super(props)
    }

    render(){
        return <Router>
            <Route exact path='/'>Home page b dz</Route>
            <Route path='/join' Component={RoomJoinPage} />
        </Router>
    }

    // render(){
    //     return 
    //     <Router>
    //         <div>
    //             <Route exact path="/" ><p>this is the homepgae</p></Route>
    //             <Route path="/join" Component={RoomJoinPage}/>
    //             {/* <Route></Route> */}
    //         </div>
    //     </Router>
    // }
}