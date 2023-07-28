import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";
import { AccountContext } from "../AccountContext";

function UpdateAccount() {
  const { accountData, setAccountData } = useContext(AccountContext);
  const id = accountData.id;
  const username = accountData.username;
  const [first_name, setFirstName] = useState(accountData.first_name);
  const [last_name, setLastName] = useState(accountData.last_name);
  const [email, setEmail] = useState(accountData.email);
  const [phone_number, setPhoneNumber] = useState(accountData.phone_number);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const editAccount = {};
    editAccount.first_name = first_name;
    editAccount.last_name = last_name;
    editAccount.email = email;
    editAccount.phone_number = phone_number;
    const url = `${process.env.REACT_APP_API_HOST}/accounts/${accountData.username}/`;
    const fetchConfig = {
      method: "PATCH",
      body: JSON.stringify(editAccount),
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(url, fetchConfig);
    if (response.ok) {
      const accountData = {
        id,
        username,
        first_name,
        last_name,
        email,
        phone_number,
      };
      setFirstName("");
      setLastName("");
      setEmail("");
      setPhoneNumber("");

      localStorage.setItem("accountData", JSON.stringify(accountData));
      setAccountData(accountData);
    }
    navigate("/myaccount");
  };

  return (
    <div className="card text-bg-light mb-3">
      <h5 className="card-header">Update your Account</h5>
      <div className="card-body">
        <form onSubmit={handleSubmit} id="account-update-form">

          <div className="mb-3">
            <label className="form-label">First Name</label>
            <input
              value={first_name}
              placeholder={`${accountData && accountData.first_name}`}
              name="firstname"
              type="text"
              className="form-control"
              onChange={(e) => setFirstName(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Last Name</label>
            <input
              value={last_name}
              placeholder={`${accountData && accountData.last_name}`}
              name="lastname"
              type="text"
              className="form-control"
              onChange={(e) => setLastName(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Email</label>
            <input
              value={email}
              placeholder={`${accountData && accountData.email}`}
              name="email"
              type="email"
              className="form-control"
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>

          <div className="mb-3">
            <label className="form-label">Phone Number</label>
            <input
              value={phone_number}
              placeholder={`${accountData && accountData.phone_number}`}
              name="phonenumber"
              type="text"
              className="form-control"
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
}
export default UpdateAccount;
