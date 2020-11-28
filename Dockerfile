# Build Frontend Staticfiles
FROM node:14.15.1-stretch as front-build

WORKDIR /frontend
COPY ./frontend /frontend

RUN yarn install
RUN yarn build

# Build Backend Django Packages
FROM python:3.8.6-buster as builder
WORKDIR /backend

COPY ./backend /backend
COPY --from=front-build /frontend/dist /frontend/dist
COPY --from=front-build /frontend/templates /frontend/templates
COPY --from=front-build /frontend/webpack-stats.json /frontend/webpack-stats.json

RUN python -m pip install --upgrade pip
RUN python -m pip install pipenv
RUN python -m pipenv install --dev --system
RUN python -m pip install uwsgi

ENV DEBUG=false
ENV SECRET_KEY=HUGAHUGA

ENTRYPOINT [ "./entry.sh" ]
CMD ["uwsgi", "uwsgi.ini"]
