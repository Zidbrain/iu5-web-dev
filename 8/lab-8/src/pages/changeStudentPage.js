import {Button, Container, Form} from "react-bootstrap";
import {Link} from "react-router-dom";
import {useAsync} from "react-async";
import {getStudent} from "../modules/ajax.js";

const ChangeStudentPage = ({match}) => {
    const id = match.params.id;
    const {data, status} = useAsync({promiseFn: getStudent, id: id});

    if (status === "pending")
        return "Loading";

    console.log(status);

    return (
        [
            <Link to={"/students"}>
                <Button className={"fixed-top"}
                        style={{marginLeft: '10px', marginTop: '10px', height: '45px'}}>Назад</Button>
            </Link>,
            <Container>
                <Form className={"bg-light text-center border rounded-3"}>
                    <h1 className={"fw-bold display-4"}>{data.last_name} {data.first_name} {data.middle_name}</h1>
                    <p className={"col-lg-10 fs-4"}>Средняя оценка: {data.gpa}</p>
                </Form>
            </Container>
        ]
    )
}

export default ChangeStudentPage;