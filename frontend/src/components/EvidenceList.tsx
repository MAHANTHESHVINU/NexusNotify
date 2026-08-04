type Props = {
    evidence?: string;
};

export default function EvidenceList({
    evidence,
}: Props) {

    if (!evidence) {

        return (
            <p>No evidence available.</p>
        );

    }

    const ids = evidence
        .split(",")
        .map((id) => id.trim());

    return (
        <div>

            <h3>Evidence</h3>

            {ids.map((id) => (

                <div
                    key={id}
                    style={{
                        marginTop: "10px",
                        padding: "10px",
                        background: "#f3f4f6",
                        borderRadius: "8px",
                        cursor: "pointer",
                    }}
                >
                    📄 {id}
                </div>

            ))}

        </div>
    );
}