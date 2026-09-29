<<<<<<< HEAD
import React from 'react';
import './App.css';

export default function App() {
  return (
    <div>
      <h1>Ola galerA</h1>
      <p>Portugal e gay</p>
    </div>
=======
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";

import Home from "./pages/Home";
import Voos from "./pages/Voos";

export default function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <main style={{ minHeight: "80vh" }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/voos" element={<Voos />} />
        </Routes>
      </main>

      <Footer />
    </BrowserRouter>
>>>>>>> 11adf81c77dcece4dd672dcd354ea617c7c598b1
  );
}
