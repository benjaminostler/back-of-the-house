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

    // const [accounts, setAccounts] = useState([])

    // const fetchAccountsData = async () => {
    //     const accountsURL = 'http://localhost:8000/accounts/'
    //     const response = await fetch(accountsURL)
    //     console.log(response)

    //     if(response.ok) {
    //         const data = await response.json()
    //         console.log(data)
    //         setAccounts(data.accounts)
    //     }
    // }

    const deleteReservation = async (id) => {
        const reservationURL = `http://localhost:8000/reservations/${id}/`;
        const fetchConfig = {
            method: "delete",
            headers: {
                "Content-Type": "application/json",
            },
        };

        const response = await fetch(reservationURL, fetchConfig)
        if(response.ok) {
            window.location.reload();
        }
    }

    const viewReservation = async (id) => {
        const reservationURL = `http://localhost:8000/reservations/${id}/`
        const fetchConfig = {
            method: "get",
            headers: {
                "Content-Type": "application/json",
            }
        }
        const response = await fetch(reservationURL, fetchConfig)
        if(response.ok) {
            window.location.replace(`http://localhost:3000/reservations/${id}/`)
        }
    }

    const editReservation = async (id) => {
        const reservationURL = `http://localhost:8000/reservations/${id}/`
        const fetchConfig = {
            method: "put",
            headers: {
                "Content-Type": "application/json",
            }
        }
        const response = await fetch(reservationURL, fetchConfig)
        if(response.ok) {
            window.location.replace(`http://localhost:3000/reservations/new/`)
        }        
    }

    // const accountsFiltered = () => {
    //     const filtered = accounts.filter(sale => sale.salesperson.id === salesperson);
    //     return filtered;
    // }

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
										className="btn btn-secondary m-2">
										Edit
									</button>
                                </td>
                                <td>
									<button
										onClick={(e) => deleteReservation(reservation.id)}
										className="btn btn-secondary m-2">
										Delete
									</button>
                                </td>
                                <td>
                                    <button
										onClick={(e) => viewReservation(reservation.id)}
										className="btn btn-secondary m-2">
										View    
                                    </button>
                                </td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    )
}

export default ReservationList;