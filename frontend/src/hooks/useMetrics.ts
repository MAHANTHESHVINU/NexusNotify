import { useEffect, useState } from "react";
import { api } from "../api/api";
import type { Metrics } from "../types/metrics";

export function useMetrics() {
    const [metrics, setMetrics] = useState<Metrics | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        api.get("/metrics/")
            .then((response) => {
                setMetrics(response.data);
            })
            .catch(console.error)
            .finally(() => {
                setLoading(false);
            });
    }, []);

    return {
        metrics,
        loading,
    };
}