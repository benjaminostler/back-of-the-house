import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainPage from "./MainPage.js";
import Nav from "./Nav.js";
import SignupForm from "./accounts/SignupForm.js";
import LoginForm from "./accounts/LoginForm.js";
import ReservationForm from "./reservations/ReservationForm.js";
import { AuthProvider } from "@galvanize-inc/jwtdown-for-react";

function App() {
  const domain = /https:\/\/[^/]+/;
  const basename = process.env.PUBLIC_URL.replace(domain, "");

  return (
    <BrowserRouter basename={basename}>
      <AuthProvider baseUrl={process.env.REACT_APP_API_HOST}>
        <Nav />
        <div className="container">
          <Routes>
            <Route path="/" element={<MainPage />} />
            <Route path="/reservations/new" element ={<ReservationForm />} />
            <Route path="/accounts/new" element={<SignupForm />} />
            <Route path="/loginform" element={<LoginForm />} />
          </Routes>
        </div>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
