# Build Frontend Staticfiles
FROM node:14.15.1-stretch as front-build

WORKDIR /frontend
COPY ./frontend /frontend

RUN yarn install
RUN yarn build:staging

# Build Backend Django Packages
FROM python:3.8.6-buster
WORKDIR /backend

COPY ./backend /backend
COPY --from=front-build /frontend/dist /frontend/dist
COPY --from=front-build /frontend/templates /frontend/templates
COPY --from=front-build /frontend/webpack-stats.json /frontend/webpack-stats.json

RUN pip install --no-cache-dir -q -r requirements.txt

ENV DEBUG=false
ENV SECRET_KEY=HUGAHUGA

CMD [ "./entry.sh" ]
