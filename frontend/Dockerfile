# Build Stage
FROM node:20-alpine AS builder

WORKDIR /app

# Copy package.json dan lockfile, install dependencies
COPY package*.json ./
RUN npm install

# Copy semua kode frontend
COPY . .

# Build Next.js
RUN npm run build

# Production Image (lebih kecil)
FROM node:20-alpine

WORKDIR /app

# Copy node_modules dan .next hasil build dari builder
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/next.config.ts ./next.config.ts
COPY --from=builder /app/tsconfig.json ./tsconfig.json

# Jika kamu pakai env file, copy juga .env.production (jika ada)
# COPY --from=builder /app/.env.production ./.env.production

EXPOSE 3001

# Jalankan Next.js production server
CMD ["npm", "start"]
