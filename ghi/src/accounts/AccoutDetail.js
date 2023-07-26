import { useParams, useNavigate, Link } from "react-router-dom";
import { useEffect, useState, useContext } from "react";
import { UserContext } from "./UserContext";

export default function AccountDetail({ setCurrentAccountId, deleteAccount }) {
    const { account_id } = useParams();
    const navigate = useNavigate();
    const [account, setAccount] = useState(null);
    const { userData } = useContext(UserContext);
    const [deleteConfirmation, setDeleteConfirmation] = useState(false);

    const handleDelete = () => {
        setDeleteConfirmation(true);
      };

      const confirmDeleteAccount = () => {
        navigate(`/accounts/${account_id}/delete`);
        setDeleteConfirmation(false);
      };

      const cancelDeleteAccount = () => {
        setDeleteConfirmation(false);
      };

      const handleEditAccount = () => {
        navigate(`/accounts/${account_id_id}/edit`);
      };

      useEffect(() => {
        const fetchData = async () => {
          try {
            const response = await fetch(
              `${process.env.REACT_APP_API_HOST}/accounts/${account_id}?account_id=${account_id}`
            );
            const data = await response.json();
            setAccount(data);
            setCurrentAccountId(account_id_id);
          } catch (error) {
            console.error("Error grabbing job details: ", error);
          }
        };

        fetchData();
      }, [account_id, setCurrentAccountId]);

    //   console.log("created by:", account && job.created_by);
    //   console.log("userData: ", userData.username);
