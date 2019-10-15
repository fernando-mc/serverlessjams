# Serverless Jams

A demo serverless web application created with the [Serverless Framework](https://serverless.com).

To learn more visit [Serverless Learn](https://serverless.com/learn).

## Setting up Our Environment

First, clone this repository.

Using SSH - `git clone git@github.com:fernando-mc/serverlessjams.git`
Or using HTTPS - `git clone https://github.com/fernando-mc/serverlessjams.git`

Then, run `cd serverlessjams` and make sure you see two folders named `backend` and `frontend` and a file called `serverless.yml`.

### Getting Dependencies

- [Install](https://nodejs.org/en/download/) a stable version of Node.js and npm
- Use npm to install the Serverless Framework globally `npm install serverless -g`

## The Application

### Backend

All the code for the backend service is contained within the `backend` directory as well as some sections of `serverless.yml`.

Inside `backend` there are two files.

- The `get_song_vote_counts.py` file gets all of the vote count information from the Database.
- The `record_song_vote.py` file allows us to increment by one vote on any song.
- The `serverless.yml` files creates a DynamoDB table for our data, ties our two files to different HTTP API endpoints and creates the appropriate permissions to scan and update the DynamoDB table.

### Frontend

Our frontend contains a single `index.html` file. The UI relies on Semantic UI to create a simple interface. There are several basic JavaScript functions used to interact with the API endpoints, load the data into the application and to update the UI.

The endpoints will need to be set inside of the `index.html` later on after the backend has been deployed.

## Creating the Backend Service

Run `serverless deploy` in the top level directory that contains `serverless.yml`.

When the service finishes deploying, make sure to save the API endpoints for the next step.

## Deploying the Frontend with Serverless Finch

- Install the Serverless Finch plugin with `npm install serverless-finch --save-dev`
- Configure the Serverless Finch plugin in the custom section of `serverless.yml`
- Update the `index.html` file with the API endpoint values that were output by deploying the backend service
- Run `serverless client deploy` to deploy the frontend of the application.
- Confirm that your website bucket is correct and that you wont be overwriting anything important from it and proceed with the instructions
- Review the output of `serverless client deploy` and navigate to your website!

### What's next?