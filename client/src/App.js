import { useState } from "react";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
function App() {
  const [responses, setResponses] = useState([]);
  const apis = {
    about: {uri: "/about", method: "GET"},
    addMessage: {uri: "/messages", method: "POST"},
    viewMessages: {uri: "/messages", method: "GET"},
  };
  const handleClick = (e) => {
    const action = e.target.getAttribute("title");
    if (action && apis[action]) {
      const {uri, method} = apis[action];
      fetch(`${process.env.REACT_APP_API_URL}${uri}`, {method})
        .then(response => response.json())
        .then(data => {
          setResponses(prevResponses => [...prevResponses, data]);
        })
        .catch(error => console.error(error));
    }
  };

  return (
    <Container>
      <h1>Welcome to QueryFast</h1>
      <Button variant="primary" title="about" onClick={handleClick}>About</Button>
      <Button variant="secondary" title="addMessage" onClick={handleClick}>Add Message</Button>
      <Button variant="success" title="viewMessages" onClick={handleClick}>View Messages</Button>
      <div>
        {responses.map((response, index) => (
          <div key={index}>
            <h2>Response {index + 1}</h2>
            <pre>{JSON.stringify(response, null, 2)}</pre>
          </div>
        ))}
      </div>
    </Container>
  );
}

export default App;
