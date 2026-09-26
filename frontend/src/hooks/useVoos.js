import { useEffect, useState } from 'react'

import { listVoos } from '../services/api'

export function useVoos() {
	const [data, setData] = useState(null)
	const [isLoading, setIsLoading] = useState(true)
	const [error, setError] = useState(null)

	useEffect(() => {
		let cancelled = false

		async function load() {
			try {
				setIsLoading(true)
				setError(null)
				const json = await listVoos()
				if (cancelled) return

				setData(json)
			} catch (e) {
				if (cancelled) return
				const err = e instanceof Error ? e : new Error(String(e))
				setError(err)
				setData(null)
			} finally {
				if (!cancelled) setIsLoading(false)
			}
		}

		load()

		return () => {
			cancelled = true
		}
	}, [])

	return { data, isLoading, error }
}
