const express = require("express");
const axios = require("axios");

const router = express.Router();

router.post("/", async (req, res) => {
  try {
    const response = await axios.post(
      "http://ml-service:8000/simulate",
      req.body
    );
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: "Simulation failed" });
  }
});

module.exports = router;
