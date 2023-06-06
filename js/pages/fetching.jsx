import { useState } from "react";
import axios from "axios";
import useSWR from "swr";

const fetcher = (...args) => fetch(...args).then((res) => res.json());

export default function Fetching() {
	const [name, setName] = useState("");
	const [nation, setNation] = useState({
		country: [{}],
	});
	let { data, error } = useSWR(
		"https://fakestoreapi.com/products?limit=5",
		fetcher
	);

	const fetchData = () => {
		axios({
			method: "get",
			url: `https://api.nationalize.io?name=${name}`,
		}).then((res) => setNation(res["data"]));
	};

	if (error) return <p>Error</p>;
	if (!data) return <h1>Loading...</h1>;
	return (
		<>
			<input
				type="text"
				value={name}
				onChange={(e) => setName(e.target.value)}
			/>
			<button onClick={() => fetchData()}>Submit</button>
			<h1>
				{nation["country"].map((i) => {
					return (
						<>
							<div
								key={1}
								style={{
									display: "flex",
									gap: "10px",
								}}
							>
								<h1>{i["country_id"]}</h1>
								<h1>{i["probability"]}</h1>
							</div>
						</>
					);
				})}
			</h1>

			<h1>products</h1>

			<div
				style={{
					display: "flex",
					justifyContent: "space-evenly",
					gap: "20px",
					flexWrap: "wrap",
					padding: "20px",
				}}
			>
				{data.map((i) => {
					return (
						<div
							key={i["id"]}
							style={{
								padding: "10px",
								borderRadius: "10px",
								background: "grey",
								flexBasis: "200px",
								color: "white",
							}}
						>
							<h1 style={{ fontSize: "1.25em", fontWeight: "bold" }}>
								{i["title"]}
							</h1>
							<p>{i["price"]}</p>
						</div>
					);
				})}
			</div>
		</>
	);
}
