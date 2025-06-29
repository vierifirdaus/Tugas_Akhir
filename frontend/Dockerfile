# frontend/Dockerfile

# --- Tahap Build ---
FROM node:18-alpine AS builder
ENV NEXT_PUBLIC_API_URL=https://api.vierifirdaus.site
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
# Pastikan NEXT_PUBLIC_API_URL diatur di docker-compose.yml
RUN npm run build

# --- Tahap Produksi ---
FROM node:18-alpine
ENV NEXT_PUBLIC_API_URL=https://api.vierifirdaus.site
WORKDIR /app
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
COPY --from=builder /app/public ./public

# Jalankan aplikasi di port 3001
CMD ["npm", "start", "--", "-p", "3001"]