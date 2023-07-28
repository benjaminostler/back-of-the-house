import React, { useEffect, useState } from "react";
import { Modal, Button } from "react-bootstrap";

function ReservationList() {
  const [reservations, setReservations] = useState([]);
  const [showDeleteModal, setShowDeleteModal] = useState(false);
  const [reservationToDelete, setReservationToDelete] = useState(null);
  // const [accounts, setAccounts] = useState()
  // console.log(accounts)
  // const currentAccount = async () => {
  //   const url = `${process.env.REACT_APP_API_HOST}/token`;
  //   const response = await fetch(url, {
  //       credentials: "include",
  //       method: "get",
  //   });
  //   if(response.ok) {
  //       const data = await response.json();
  //       setAccounts(data.account.id)
  //   }
  // }

  // useEffect(() => {
  //   currentAccount()
  // }, [])
  
  const fetchData = async () => {
    const url = `${process.env.REACT_APP_API_HOST}/reservations`;
    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setReservations(data);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const deleteReservation = async (id) => {
    const reservationURL = `${process.env.REACT_APP_API_HOST}/reservations/${id}`;
    const fetchConfig = {
      method: "delete",
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(reservationURL, fetchConfig);
    if (response.ok) {
      window.location.reload();
    }
  };

  const handleDeleteClick = (reservation) => {
    setReservationToDelete(reservation);
    setShowDeleteModal(true);
  };

  const handleDeleteConfirm = () => {
    deleteReservation(reservationToDelete.id);
    setShowDeleteModal(false);
  };

  const handleDeleteCancel = () => {
    setShowDeleteModal(false);
  };

  const editReservation = async (id) => {
    const reservationURL = `${process.env.REACT_APP_API_HOST}/reservations/${id}`;
    const fetchConfig = {
      method: "get",
      headers: {
        "Content-Type": "application/json",
      },
    };
    const response = await fetch(reservationURL, fetchConfig);
    if (response.ok) {
      window.location.replace(`${process.env.REACT_APP_API_HOST}/reservations`);
    }
  };

  return (
    <div>
      <h1 className="mt-3 mb-3 p-0">Reservations</h1>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Email</th>
            <th>Phone Number</th>
            <th>Party Size</th>
            <th>Date</th>
            <th>Time</th>
          </tr>
        </thead>
        <tbody>
          {reservations.map((reservation) => {
            return (
              <tr key={reservation.id}>
                <td>{reservation.first_name}</td>
                <td>{reservation.last_name}</td>
                <td>{reservation.email}</td>
                <td>{reservation.phone_number}</td>
                <td>{reservation.party_size}</td>
                <td>{reservation.date}</td>
                <td>{reservation.time}</td>
                <td>
                  <button
                    onClick={(e) => editReservation(reservation.id)}
                    className="btn btn-secondary m-2"
                  >
                    Edit
                  </button>
                </td>
                <td>
                  <button
                    onClick={(e) => handleDeleteClick(reservation)}
                    className="btn btn-secondary m-2"
                  >
                    Delete
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
      <Modal show={showDeleteModal} onHide={handleDeleteCancel}>
        <Modal.Header closeButton>
          <Modal.Title>Delete Reservation</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          Are you sure you want to delete this reservation?
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleDeleteCancel}>
            Cancel
          </Button>
          <Button variant="primary" onClick={handleDeleteConfirm}>
            Delete
          </Button>
        </Modal.Footer>
      </Modal>
    </div>
  );
}

export default ReservationList;