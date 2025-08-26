"""
npm i cross-env dotenv pg axios reflect-metadata rimraf tsx @neondatabase/serverless

npm i -d ts-node

https://chatgpt.com/share/68ad389e-16dc-8001-a6ca-f7c78088b29e


"""

"""
hono index.ts -

import { cors } from "hono/cors";
import * as dotenv from "dotenv";

// .env.development 읽을건지, .env.production 읽을건지 결정
const envFile =
  process.env.NODE_ENV === "production"
    ? ".env.production"
    : ".env.development";
dotenv.config({ path: envFile });

app.use(
  "*",
  cors({
    origin: "*",
    allowMethods: ["GET", "POST", "PUT", "DELETE", "OPTIONS", "PATCH"],
    allowHeaders: ["*"],
  })
);
"""