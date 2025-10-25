import { useState } from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
function App({ instance }) {
  const [csvResponse, setCsvResponse] = useState(null);
  const [excelResponse, setExcelResponse] = useState(null);
  const onApiCsv = async () => {
    const response = await fetch("/api/csv/");
    const data = await response.json();
    console.log(data);
    setCsvResponse(data);
  };

  const onApiExcel = async () => {
    const response = await fetch("/api/excel/");
    const data = await response.json();
    console.log(data);
    setExcelResponse(data);
  };

  return (
    <Container>
      <h1>Welcome to QueryFast</h1>
      <Button onClick={onApiCsv}>Extract CSV</Button>
      <Button onClick={onApiExcel}>Extract Excel</Button>

      {csvResponse && <>{csvResponse}</>}
      {excelResponse && <>{excelResponse}</>}
    </Container>
  );
}

export default App;
