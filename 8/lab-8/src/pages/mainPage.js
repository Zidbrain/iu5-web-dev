import {Button} from "react-bootstrap";

function MainPage() {
    return (
        <div className={"text-center border-bottom"}>
            <h1 className={"display-4 fw-bold"}>Лабораторная работа №8</h1>
            <Button style={{marginBottom: '10px'}} href={"/students"}>Перейти к студентам</Button>
        </div>
    )
}

export default MainPage;