import { useRef } from "react";
import backgroundVideo from "./assets/background.mp4";

function MainPage() {
  const videoRef = useRef();
  return (
    <>
      <div
        className="p-8 flex flex-col items-center justify-center duration-500 w-full bg-black/80 opacity-20">
        <h1 className="text-5xl lg:text-7x1 capitalize mb-12">
          Back of the House
        </h1>
        <div className="col-lg-6 mx-auto">
          <p className="lead mb-4">Exploring the final frontiers of flavor</p>
        </div>
      </div>
      <div className="justify-center w-full h-screen text-center">
        <video
          ref={videoRef}
          src={backgroundVideo}
          autoPlay
          loop
          id="video"
          className="object-cover hfull w-full absolute -z-10"
        />
      </div>
    </>
  );
}

export default MainPage;
