import React, { useState } from "react";
import useAToken from "@galvanize-inc/jwtdown-for-react";
import { useNavigate } from "react-router-dom";

const AccountEditForm = () => {
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [phone_number, setPhoneNumber] = useState("");
  const { token, updateAccount } = useAToken(); // Renamed from useEffect to useState
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const updatedAccountData = {
      first_name: first_name,
      last_name: last_name,
      username: username,
      email: email,
      phone_number: phone_number,
    };

    try {
      const response = await updateAccount(
        updatedAccountData,
        "http://localhost:8000/api/accounts/"
      );

      if (!response.ok) {
        throw new Error("Failed to update account");
      }

      console.log("Account updated successfully");
      navigate("/");
    } catch (error) {
      console.error("Error updating account:", error.message);
    }
  };

  return (
    <div className="card text-bg-light mb-3">
      <h5 className="card-header">Edit Account</h5>
      <div className="card-body">
        <form onSubmit={(e) => handleSubmit(e)}>

          <div className="mb-3">
            <label className="form-label">First Name:</label>
            <input
              name="firstname"
              type="text"
              className="form-control"
              value={first_name}
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
              value={last_name}
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
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email:</label>
            <input
              name="email"
              type="text"
              className="form-control"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Phone Number:</label>
            <input
              name="phonenumber"
              type="text"
              className="form-control"
              value={phone_number}
              onChange={(e) => setPhoneNumber(e.target.value)}
              required
            />
          </div>

          <div>
            <input className="btn btn-primary" type="submit" value="Update" />
          </div>
        </form>
      </div>
    </div>
  );
};

export default AccountEditForm;
