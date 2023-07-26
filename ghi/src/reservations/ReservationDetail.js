import { useParams } from 'react-router-dom';
import { useEffect, useState } from 'react';

export default function Reservation() {
    const { id } = useParams();
    const [reservation, setReservation] = useState();

    const fetchReservationData = async () => {
        const url = 'http://localhost:8000/reservations/' + id;
        const response = await fetch(url)

        if(response.ok) {
            const data = await response.json();
            setReservation(data)
        }
    }

    useEffect(() => {
        fetchReservationData();
    }, [])

    // useEffect(() => {
    //     console.log('useEffect');
    //     const url = 'http://localhost:8000/reservations/' + id;
    //     fetch(url)
    //         .then((response) => {
    //             return response.json();
    //         })
    //         .then((data) => {
    //             setReservation(data);
    //         })
    // })

//     return (
//         <>
//             {reservation ? (
//                 <div>
//                     <p>{reservation.id}</p>
//                     <p>{reservation.first_name}</p>
//                 </div>
//             ) : null}
//         </>
//     )
// }

    return (
        <div>
            <h1 className="mt-3 mb-3 p-0">Reservations</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Reservation ID</th>
                        <th>Account ID</th>
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
                            <td>{reservation.id}</td>
                            <td>{reservation.account_id}</td>
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
    )
}