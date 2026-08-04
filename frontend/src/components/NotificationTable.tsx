import type { Prediction } from "../types/prediction";

type Props = {
    predictions: Prediction[];
    loading: boolean;
    onSelect: (prediction: Prediction) => void;
};

export default function NotificationTable({
    predictions,
    loading,
    onSelect,
}: Props) {

    if (loading) {
        return (
            <div
                style={{
                    background: "white",
                    padding: "20px",
                    borderRadius: "12px",
                    boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
                }}
            >
                Loading notifications...
            </div>
        );
    }

    return (
        <div
            style={{
                background: "white",
                padding: "20px",
                borderRadius: "12px",
                boxShadow: "0 2px 8px rgba(0,0,0,0.1)",
            }}
        >
            <h2 style={{ marginBottom: "20px" }}>
                Notifications
            </h2>

            <table
                style={{
                    width: "100%",
                    borderCollapse: "collapse",
                }}
            >
                <thead>
                    <tr
                        style={{
                            borderBottom: "2px solid #ddd",
                        }}
                    >
                        <th align="left">Message ID</th>
                        <th align="left">Action</th>
                        <th align="left">Type</th>
                        <th align="left">Confidence</th>
                    </tr>
                </thead>

                <tbody>
                    {predictions.map((prediction) => {

                        const actionColor =
                            prediction.action === "SUPPRESS"
                                ? "#ef4444"
                                : "#22c55e";

                        const confidenceColor =
                            prediction.confidence >= 0.90
                                ? "#16a34a"
                                : prediction.confidence >= 0.75
                                ? "#f59e0b"
                                : "#dc2626";

                        const typeColor =
                            prediction.message_type === "PHISHING"
                                ? "#dc2626"
                                : prediction.message_type === "PROMOTION"
                                ? "#f59e0b"
                                : prediction.message_type === "TRANSACTIONAL"
                                ? "#2563eb"
                                : "#6b7280";

                        return (
                            <tr
                                key={prediction.message_id}
                                onClick={() => onSelect(prediction)}
                                style={{
                                    cursor: "pointer",
                                    borderBottom: "1px solid #eee",
                                }}
                            >
                                <td
                                    style={{
                                        padding: "12px",
                                    }}
                                >
                                    {prediction.message_id}
                                </td>

                                <td
                                    style={{
                                        padding: "12px",
                                    }}
                                >
                                    <span
                                        style={{
                                            background: actionColor,
                                            color: "white",
                                            padding: "4px 10px",
                                            borderRadius: "20px",
                                            fontWeight: "bold",
                                        }}
                                    >
                                        {prediction.action}
                                    </span>
                                </td>

                                <td
                                    style={{
                                        padding: "12px",
                                    }}
                                >
                                    <span
                                        style={{
                                            background: typeColor,
                                            color: "white",
                                            padding: "4px 10px",
                                            borderRadius: "20px",
                                        }}
                                    >
                                        {prediction.message_type}
                                    </span>
                                </td>

                                <td
                                    style={{
                                        padding: "12px",
                                        color: confidenceColor,
                                        fontWeight: "bold",
                                    }}
                                >
                                    {(prediction.confidence * 100).toFixed(1)}%
                                </td>
                            </tr>
                        );

                    })}
                </tbody>
            </table>
        </div>
    );
}