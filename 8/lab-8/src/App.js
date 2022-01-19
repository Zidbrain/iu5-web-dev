import {BrowserRouter, Route, Switch} from "react-router-dom";
import MainPage from "./pages/mainPage.js"
import NavbarComponent from "./components/navbarComponent";
import StudentsPage from "./pages/studentsPage";
import ChangeStudentPage from "./pages/changeStudentPage.js"

function App() {

    return (

        <BrowserRouter>
            <NavbarComponent/>
            <Switch>
                <Route exact path="/">
                    <MainPage/>
                </Route>
                <Route exact path={"/students"}>
                    <StudentsPage/>
                </Route>
                <Route path={"/changeStudent/:id"} component={ChangeStudentPage}/>
            </Switch>
        </BrowserRouter>
    );
}

export default App;
