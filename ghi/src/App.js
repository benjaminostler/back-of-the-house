import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect, useState } from "react";
import Construct from "./Construct.js";
import ErrorNotification from "./ErrorNotification";
import MainPage from "./MainPage.js";
import Nav from "./Nav.js";
import "./App.css";
import AccountForm from "./AccountForm.js";
import AccountList from "./AccountList.js";

function App() {
  const [launchInfo, setLaunchInfo] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function getData() {
      let url = `${process.env.REACT_APP_API_HOST}/api/launch-details`;
      console.log("fastapi url: ", url);
      let response = await fetch(url);
      console.log("------- hello? -------");
      let data = await response.json();

      if (response.ok) {
        console.log("got launch data!");
        setLaunchInfo(data.launch_details);
      } else {
        console.log("drat! something happened");
        setError(data.message);
      }
    }
    getData();
  }, []);

  return (
    <>
      <BrowserRouter>
        <Nav />
        <div className="container">
          <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="accounts">
              <Route index element={<AccountList />} />
              <Route path="new" element={<AccountForm />} />
            </Route>
          </Routes>
        </div>
      </BrowserRouter>
      <div>
        <ErrorNotification error={error} />
        <Construct info={launchInfo} />
      </div>
      ;
    </>
  );
}

export default App;
