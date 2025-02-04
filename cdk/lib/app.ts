import { App, Stack, Environment } from 'aws-cdk-lib';
import { BotStack } from './botStack';
import { Stage } from './constants';

const app = new App();
const stages: Stage[] = ['test', 'live'];

stages.forEach((stage) => {
    const botStack = new BotStack(app, `BotStack-${stage}`, {
        env: {
            account: process.env.ACCOUNT_ID,
            region: "us-west-2"
        },
        stage
    });
});

