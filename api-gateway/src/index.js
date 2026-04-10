const express = require("express");
const cors = require("cors");
const morgan = require("morgan");

const predictRoutes = require("./routes/predictRoutes");
const simulateRoutes = require("./routes/simulateRoutes");

const app = express();

app.use(cors());
app.use(express.json());
app.use(morgan("dev"));

app.use("/api/predict", predictRoutes);
app.use("/api/simulate", simulateRoutes);

app.get("/", (req, res) => {
  res.send("NutriSphere API Gateway Running 🚀");
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Gateway running on ${PORT}`));
