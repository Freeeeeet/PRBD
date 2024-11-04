# Устанавливаем Node.js для сборки приложения
FROM node:14 as build-stage

# Рабочая директория для сборки
WORKDIR /app

# Копируем package.json и package-lock.json (если он существует) и устанавливаем зависимости
COPY package.json package-lock.json* ./
RUN npm install

# Копируем все файлы и собираем приложение
COPY . .
RUN npm run build

# Используем nginx для сервера статических файлов
FROM nginx:alpine
COPY --from=build-stage /app/build /usr/share/nginx/html

# Копируем собственный конфиг для Nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf