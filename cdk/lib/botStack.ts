import { Stack, StackProps } from "aws-cdk-lib";
import { Architecture, Code, Function, FunctionUrlAuthType, Runtime } from "aws-cdk-lib/aws-lambda";
import { Construct } from "constructs";
import { Stage } from "./constants";

export interface BotStackProps extends StackProps {
    readonly stage: Stage;
}

export class BotStack extends Stack {
    constructor(scope: Construct, id: string, props: BotStackProps) {
        super(scope, id, props);
        const botLambda = new Function(this, `BotFunction-${props.stage}`, {
            functionName: `RestaurantClubBot-${props.stage}`,
            handler: 'restaurant_club_bot.lambda_entry.lambda_entry',
            code: Code.fromAsset('../bot/build/archive.zip'),
            runtime: Runtime.PYTHON_3_11,
            architecture: Architecture.X86_64
        });

        botLambda.addFunctionUrl({
            authType: FunctionUrlAuthType.NONE
        })
    }
}