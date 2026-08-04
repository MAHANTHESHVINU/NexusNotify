export interface Prediction {

    message_id: string;

    action: string;

    message_type: string;

    confidence: number;

    reason: string;

    evidence_message_ids?: string;

}