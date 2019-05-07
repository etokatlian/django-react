import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Form from "./Form";
const App = () => (
  <React.Fragment>
    <DataProvider endpoint="api/lead/" render={data => <Table data={data} />} />
    <Form endpoint="api/lead/" />
    <h1>Hello</h1>
    <h1>Hello</h1>
  </React.Fragment>
);
const wrapper = document.getElementById("app");
wrapper ? ReactDOM.render(<App />, wrapper) : null;
