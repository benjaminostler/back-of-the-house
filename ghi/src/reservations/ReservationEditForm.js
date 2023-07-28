import React, { useEffect, useState, useCallback } from "react";
import { useParams } from "react-router-dom"

function EditReservationForm({ reservationId }) {
  const { id } = useParams();
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
  const [accounts, setAccounts] = useState()

  const currentAccount = async () => {
    const url = `${process.env.REACT_APP_API_HOST}/token`;
    const response = await fetch(url, {
        credentials: "include",
        method: "get",
    });
    if(response.ok) {
        const data = await response.json();
        setAccounts(data.account.id)
    }
  }

  const fetchReservation = useCallback(async () => {
    const reservationURL = `http://localhost:8000/reservations/` + id;
    const response = await fetch(reservationURL);
    if (response.ok) {
    const data = await response.json();
    setFirstName(data.first_name);
    setLastName(data.last_name);
    setEmail(data.email);
    setPhoneNumber(data.phone_number);
    setPartySize(data.party_size);
    setDate(data.date);
    setTime(data.time);
    }
  }, [id])

  useEffect(() => {
    currentAccount()
  }, [])

  useEffect(() => {
    fetchReservation()
  }, [fetchReservation])

  const handleSubmit = async (event) => {
    event.preventDefault();
    const updatedReservation = {
      account_id: accounts,
      first_name: firstName,
      last_name: lastName,
      email: email,
      phone_number: phoneNumber,
      party_size: partySize,
      date: date,
      time: time,
    };

    const reservationURL = `http://localhost:8000/reservations/` + id;
    const fetchConfig = {
      method: "put",
      body: JSON.stringify(updatedReservation),
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(reservationURL, fetchConfig);
    if (response.ok) {
      console.log("Reservation updated successfully");
      window.location.replace('/reservations')
    } else {
      console.error("Failed to update reservation");
    }
  };

    return (
        <div className="row">
            <div className="offset-3 col-6">
                <div className="shadow p-4 mt-4">
                    <h1>Create a Reservation</h1>
                    <form onSubmit={handleSubmit} id="create-reservation-form">
                        <div className="form-floating mb-3">                       
                            <input onChange={handleFirstNameChange} placeholder="First Name" value={firstName} required type="text" name="first_name" id="first_name" className="form-control"/>
                            <label htmlFor="first_name">First Name:</label>     
                        </div>
                        <div className="form-floating mb-3">                          
                            <input onChange={handleLastNameChange} placeholder="Last Name" value={lastName} required type="text" name="last_name" id="last_name" className="form-control"/>
                            <label htmlFor="last_name">Last Name:</label>                              
                        </div>
                        <div className="form-floating mb-3">                            
                            <input onChange={handleEmailChange} placeholder="Email" value={email} required type="text" name="email" id="email" className="form-control"/>
                            <label htmlFor="email">Email:</label>
                        </div>
                        <div className="form-floating mb-3">                            
                            <input onChange={handlePhoneNumberChange} placeholder="Phone Number" value={phoneNumber} required type="text" name="phone_number" id="phone_number" className="form-control"/>
                            <label htmlFor="phone_number">Phone Number:</label>
                        </div>
                        <div className="mb-3">
                            <label htmlFor="party_size">Party Size:  </label>                                                               
                            <select onChange={handlePartySizeChange} value={partySize}>
                                {
                                    [...Array(20)].map((_, i) => i + 1)
                                                  .map(i => <option key={i} value={i}>{i}</option>)
                                }
                            </select>
                        </div>
                        <div className="form-floating mb-3">                         
                            <input value={date} onChange={handleDateChange} placeholder="Date" required type="date" name="date" id="date" className="form-control" />
                            <label htmlFor="date">Date:</label>
                        </div>
                        <div className="form-floating mb-3">                    
                            <input value={time} onChange={handleTimeChange} placeholder="Time" required type="time" name="time" id="time" className="form-control" />
                            <label htmlFor="time">Time:</label>
                        </div>                                     
                        <button type="submit" className="btn btn-outline-primary">
                            Edit
                        </button>                        
                    </form>
                </div>
            </div>
        </div>
    )
}

export default EditReservationForm;