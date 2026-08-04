import type { Prediction } from "../types/prediction";
import EvidenceList from "./EvidenceList";

type Props = {
    prediction: Prediction | null;
};

export default function DecisionPanel({
    prediction,
}: Props) {

    return (
        <div
            style={{
                background: "white",
                borderRadius: "12px",
                padding: "20px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
            }}
        >
            <h2>🤖 AI Decision</h2>

            {!prediction ? (
                <p>Select a notification.</p>
            ) : (
                <>
                    <p>
                        <strong>Message ID</strong>
                        <br />
                        {prediction.message_id}
                    </p>

                    <p>
                        <strong>Action</strong>
                        <br />
                        {prediction.action}
                    </p>

                    <p>
                        <strong>Message Type</strong>
                        <br />
                        {prediction.message_type}
                    </p>

                    <p>
                        <strong>Confidence</strong>
                        <br />
                        {(prediction.confidence * 100).toFixed(2)}%
                    </p>

                    <p>
                        <strong>Reason</strong>
                        <br />
                        {prediction.reason}
                    </p>

                    <EvidenceList
                        evidence={prediction.evidence_message_ids}
                    />
                </>
            )}
        </div>
    );
}