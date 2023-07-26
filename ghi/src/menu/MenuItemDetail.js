import { useParams } from "react-router-dom";

export default function MenuItemDetail() {
  const { id } = useParams();

  return (
    <div>
      <p>Menu Item goes here</p>

      <p>{id}</p>
    </div>
  );
}
