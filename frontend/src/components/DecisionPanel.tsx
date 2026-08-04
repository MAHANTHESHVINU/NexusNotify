import { usePrediction } from "../hooks/usePrediction";
import type { Prediction } from "../types/prediction";
import EvidenceList from "./EvidenceList";

type Props = {
    prediction: Prediction | null;
};

export default function DecisionPanel({
    prediction,
}: Props) {

    const {
        prediction: details,
        loading,
    } = usePrediction(
        prediction?.message_id ?? null
    );

    return (
        <div
            style={{
                background: "white",
                borderRadius: "12px",
                padding: "20px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
            }}
        >
            <h2>AI Decision</h2>

            {!prediction && (
                <p>Select a notification.</p>
            )}

            {loading && (
                <p>Loading prediction...</p>
            )}

            {details && (
                <>
                    <p>
                        <strong>Message ID</strong>
                        <br />
                        {details.message_id}
                    </p>

                    <p>
                        <strong>Action</strong>
                        <br />
                        {details.action}
                    </p>

                    <p>
                        <strong>Message Type</strong>
                        <br />
                        {details.message_type}
                    </p>

                    <p>
                        <strong>Confidence</strong>
                        <br />
                        {(details.confidence * 100).toFixed(2)}%
                    </p>

                    <p>
                        <strong>Reason</strong>
                        <br />
                        {details.reason}
                    </p>

                    <EvidenceList
                        evidence={details.evidence_message_ids}
                    />
                </>
            )}
        </div>
    );
}