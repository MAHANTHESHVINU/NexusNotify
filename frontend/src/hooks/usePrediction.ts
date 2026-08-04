import { useEffect, useState } from "react";
import { api } from "../api/api";
import type { Prediction } from "../types/prediction";

export function usePrediction(messageId: string | null) {

    const [prediction, setPrediction] = useState<Prediction | null>(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {

        if (!messageId) {
            setPrediction(null);
            return;
        }

        async function fetchPrediction() {

            setLoading(true);

            try {

                const response = await api.get(
                    `/prediction/${messageId}`
                );

                setPrediction(response.data);

            } catch (error) {

                console.error(error);

                setPrediction(null);

            } finally {

                setLoading(false);

            }

        }

        fetchPrediction();

    }, [messageId]);

    return {
        prediction,
        loading,
    };
}