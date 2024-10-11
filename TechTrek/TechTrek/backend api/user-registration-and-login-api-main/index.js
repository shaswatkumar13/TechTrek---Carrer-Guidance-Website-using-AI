import express from "express";
import mongoose from "mongoose";
import cors from "cors";
import "dotenv/config.js";

// Load routes
import usersRoute from "./routes/users.js";

// Setup Express App
const app = express();

// Middlewares
app.use(express.json({ limit: "30mb", extended: true }));
app.use(express.urlencoded({ limit: "30mb", extended: true }));
app.use(cors());

// Connect to the database
const URI = "mongodb+srv://tanmaychouhan2021:WbiNVaGE0MmnsmUf@cluster0.tozefxd.mongodb.net/user";
// password = WbiNVaGE0MmnsmUf1
// username = tanmaychouhan2021
mongoose
    .connect(URI)
    .then(() => console.log("Database connected..."))
    .catch((error) => console.log(error.message));

// Use routes
app.use("/user", usersRoute);

// Port
const PORT =  5000;

app.listen(PORT, () => console.log(`Sever running on port: ${PORT}`));
