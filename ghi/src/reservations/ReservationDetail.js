import { useParams } from "react-router-dom";
import { useEffect, useState, useCallback } from "react";

export default function Reservation() {
  const { id } = useParams();
  const [reservation, setReservation] = useState();

  const fetchReservationData = useCallback(async () => {
    const url = `${process.env.REACT_APP_API_HOST}/reservations/` + id;
    const response = await fetch(url);

    if (response.ok) {
      const data = await response.json();
      setReservation(data);
    }
  }, [id]); // Include 'id' as a dependency to appease es linter

  useEffect(() => {
    fetchReservationData();
  }, [fetchReservationData]); // Include 'fetchReservationData' as a dependency


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
          {reservation ? (
            <tr>
              <td>{reservation.first_name}</td>
              <td>{reservation.last_name}</td>
              <td>{reservation.email}</td>
              <td>{reservation.phone_number}</td>
              <td>{reservation.party_size}</td>
              <td>{reservation.date}</td>
              <td>{reservation.time}</td>
            </tr>
          ) : null}
        </tbody>
      </table>
    </div>
  );
}
