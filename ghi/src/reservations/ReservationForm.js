import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import calendar from "../assets/lottie_files/calendar.json";
import Lottie from "lottie-react";
import "../index.css";
function ReservationForm() {
  const navigate = useNavigate();
  const [firstName, setFirstName] = useState("");
  const handleFirstNameChange = (event) => {
    const value = event.target.value;
    setFirstName(value);
  };
  const [lastName, setLastName] = useState("");
  const handleLastNameChange = (event) => {
    const value = event.target.value;
    setLastName(value);
  };
  const [email, setEmail] = useState("");
  const handleEmailChange = (event) => {
    const value = event.target.value;
    setEmail(value);
  };
  const [phoneNumber, setPhoneNumber] = useState("");
  const handlePhoneNumberChange = (event) => {
    const value = event.target.value;
    setPhoneNumber(value);
  };
  const [partySize, setPartySize] = useState("");
  const handlePartySizeChange = (event) => {
    const value = event.target.value;
    setPartySize(value);
  };
  const [date, setDate] = useState("");
  const handleDateChange = (event) => {
    const value = event.target.value;
    setDate(value);
  };
  const [time, setTime] = useState("");
  const handleTimeChange = (event) => {
    const value = event.target.value;
    setTime(value);
  };

  const [accounts, setAccounts] = useState();

  const currentAccount = async () => {
    const url = `${process.env.REACT_APP_API_HOST}/token`;
    const response = await fetch(url, {
      credentials: "include",
      method: "get",
    });
    if (response.ok) {
      const data = await response.json();
      setAccounts(data.account.id);
    }
  };

  useEffect(() => {
    currentAccount();
  }, []);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const reservation = {
      account_id: accounts,
      first_name: firstName,
      last_name: lastName,
      email: email,
      phone_number: phoneNumber,
      party_size: partySize,
      date: date,
      time: time,
    };

    const reservationURL = `${process.env.REACT_APP_API_HOST}/reservations`;
    const fetchConfig = {
      method: "post",
      body: JSON.stringify(reservation),
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(reservationURL, fetchConfig);
    if (response.ok) {
      const newReservation = await response.json();
      console.log(newReservation);

      setFirstName("");
      setLastName("");
      setEmail("");
      setPhoneNumber("");
      setPartySize("");
      setDate("");
      setTime("");
      navigate("/reservations");
    }
  };

  return (
    <div className="container">
      <div className="row">
        <div className="col-7">
          <div className="shadow p-4 mt-4">
            <h1>Create a Reservation</h1>
            <form onSubmit={handleSubmit} id="create-reservation-form">
              <div className="form-floating mb-3">
                <input
                  onChange={handleFirstNameChange}
                  placeholder="First Name"
                  required
                  type="text"
                  name="first_name"
                  id="first_name"
                  className="form-control"
                />
                <label htmlFor="first_name">First Name:</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handleLastNameChange}
                  placeholder="Last Name"
                  required
                  type="text"
                  name="last_name"
                  id="last_name"
                  className="form-control"
                />
                <label htmlFor="last_name">Last Name:</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handleEmailChange}
                  placeholder="Email"
                  required
                  type="text"
                  name="email"
                  id="email"
                  className="form-control"
                />
                <label htmlFor="email">Email:</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  onChange={handlePhoneNumberChange}
                  placeholder="Phone Number"
                  required
                  type="text"
                  name="phone_number"
                  id="phone_number"
                  className="form-control"
                />
                <label htmlFor="phone_number">Phone Number:</label>
              </div>
              <div className="mb-3">
                <label htmlFor="party_size">Party Size: </label>
                <select onChange={handlePartySizeChange}>
                  {[...Array(20)]
                    .map((_, i) => i + 1)
                    .map((i) => (
                      <option key={i} value={i}>
                        {i}
                      </option>
                    ))}
                </select>
              </div>
              <div className="form-floating mb-3">
                <input
                  value={date}
                  onChange={handleDateChange}
                  placeholder="Date"
                  required
                  type="date"
                  name="date"
                  id="date"
                  className="form-control"
                />
                <label htmlFor="date">Date:</label>
              </div>
              <div className="form-floating mb-3">
                <input
                  value={time}
                  onChange={handleTimeChange}
                  placeholder="Time"
                  required
                  type="time"
                  name="time"
                  id="time"
                  className="form-control"
                />
                <label htmlFor="time">Time:</label>
              </div>
              <button type="submit" className="btn btn-outline-primary">
                Create
              </button>
            </form>
          </div>
        </div>
        <div className="col-5">
          <Lottie animationData={calendar} />
        </div>
      </div>
    </div>
  );
}

export default ReservationForm;
