import {Container, Navbar, NavLink} from "react-bootstrap";

function NavbarComponent(){
    return (
        <Container className={"justify-content-center"}>
            <Navbar className={"justify-content-center"}>
                <ul className={"nav nav-pills list-group-horizontal"}>
                    <li className={"nav-item"}>
                        <NavLink active={true} href={"/"}>Главная страница</NavLink>
                    </li>
                    <li className={"nav-item"}>
                        <NavLink href={"/students"}>Студенты</NavLink>
                    </li>
                </ul>
            </Navbar>
        </Container>
    )
}

export default NavbarComponent;