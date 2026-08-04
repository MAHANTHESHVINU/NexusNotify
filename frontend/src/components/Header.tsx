export default function Header() {
    return (
        <div
            style={{
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                marginBottom: "30px",
                padding: "20px",
                background: "#1e293b",
                color: "white",
                borderRadius: "12px",
            }}
        >
            <div>
                <h1
                    style={{
                        margin: 0,
                    }}
                >
                    NexusNotify
                </h1>

                <p
                    style={{
                        marginTop: "8px",
                        opacity: 0.8,
                    }}
                >
                    AI Powered Notification Intelligence System
                </p>
            </div>

            <div
                style={{
                    fontWeight: "bold",
                    fontSize: "18px",
                }}
            >
                🤖 AI Dashboard
            </div>
        </div>
    );
}