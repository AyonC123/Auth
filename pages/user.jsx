import React from "react";
import { useSession } from "next-auth/react";

export default function User() {
	const getData = async () => {
		return await (await fetch("localhost://api/isauthorized")).json();
	};
	const { data: session } = useSession({ required: true });
	return (
		<>
			{session && (
				<>
					<h1>Name: {session.user.name}</h1>
					<h1>Email: {session.user.email}</h1>
					<img
						src={session.user.image}
						alt="profile image"
						style={{ padding: "10px", borderRadius: "50px" }}
					/>
				</>
			)}
		</>
	);
}
