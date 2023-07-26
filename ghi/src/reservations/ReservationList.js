import React, { useEffect, useState } from "react";

function ReservationList() {
    const [reservations, setReservations] = useState([]);

    const fetchData = async () => {
        const url = `http://localhost:8000/reservations/`
        const response = await fetch(url)

        if(response.ok) {
            const data = await response.json();
            setReservations(data)
        }
    }

    useEffect(() => {
        fetchData();
    }, [])


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
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    )
}

export default ReservationList;