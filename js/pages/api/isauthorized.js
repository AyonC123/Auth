import { getServerSession } from "next-auth/next";
import { authOptions } from "./auth/[...nextauth]";

export default async function handler(req, res) {
	const session = await getServerSession(req, res, authOptions);
	if (session) {
		res.status(200).json({
			isAuthorized: true,
			data: session["user"],
		});
	} else {
		res.status(401).json({
			isAuthorized: false,
		});
	}
}
