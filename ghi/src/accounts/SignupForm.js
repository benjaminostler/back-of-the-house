import React from "react";
import useToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";
import { useState } from "react";

const SignupForm = () => {
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [phone_number, setPhoneNumber] = useState("");
  const { register } = useToken();
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    const accountData = {
      first_name: first_name,
      last_name: last_name,
      username: username,
      password: password,
      email: email,
      phone_number: phone_number,
    };
    register(accountData, `${process.env.REACT_APP_API_HOST}/api/accounts/`);
    e.target.reset();
    navigate("/");
  };

  return (
    <div className="card text-bg-light mb-3">
      <h5 className="card-header">Sign-Up</h5>
      <div className="card-body">
        <form onSubmit={(e) => handleSubmit(e)}>
          <div className="mb-3">
            <label className="form-label">First Name:</label>
            <input
              name="firstname"
              type="text"
              className="form-control"
              onChange={(e) => setFirstName(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Last Name:</label>
            <input
              name="lastname"
              type="text"
              className="form-control"
              onChange={(e) => setLastName(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Username:</label>
            <input
              name="username"
              type="text"
              className="form-control"
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Password:</label>
            <input
              name="password"
              type="password"
              className="form-control"
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email:</label>
            <input
              name="email"
              type="text"
              className="form-control"
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Phone Number:</label>
            <input
              name="phone_number"
              type="text"
              className="form-control"
              onChange={(e) => setPhoneNumber(e.target.value)}
              required
            />
          </div>

          <div>
            <input className="btn btn-primary" type="submit" value="Register and Login" />
          </div>

        </form>
      </div>
    </div>
  );
};

export default SignupForm;
