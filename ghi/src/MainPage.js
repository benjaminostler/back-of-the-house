function MainPage() {
  return (
    <div className="px-4 py-5 my-5 text-center">
      <video autoPlay loop muted id="video">
        <source src='https://www.youtube.com/watch?v=KjMagRL-ozI' type="video/mp4" />
      </video>
      <h1 className="display-5 fw-bold">Back of the House</h1>
      <div className="col-lg-6 mx-auto">
        <p className="lead mb-4">Exploring the final frontiers of flavor</p>
      </div>
    </div>
  );
}

export default MainPage;
