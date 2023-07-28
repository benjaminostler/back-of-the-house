import React from "react";
import { useRef } from "react";
import heroVideo from "./assets/background.mp4";
export default function HeroSection() {
    const videoRef = useRef();

    return (
        <div className="flex items-end justify-center w-full h-screen">
            <video ref={videoRef}
            src={heroVideo}
            autoPlay
            loop
            className="object-cover hfull w-full absolute -z-10"/>

        </div>
    )
}
