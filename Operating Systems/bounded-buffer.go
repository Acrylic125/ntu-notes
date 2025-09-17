package main

import (
	"context"
	"fmt"
	"sync"
	"time"

	"golang.org/x/sync/semaphore"
)

func main() {
	BUF_SIZE := 3
	buffer := make([]byte, 0, BUF_SIZE)
	counter := 0

	// Used to protect buffer and counter.
	mux := sync.Mutex{}
	fullSem := semaphore.NewWeighted(int64(BUF_SIZE))
	emptySem := semaphore.NewWeighted(int64(BUF_SIZE))

	// Full indicates how full the buffer is.
	if b := fullSem.TryAcquire(int64(BUF_SIZE)); !b {
		panic("fullSem should be acquired")
	}

	ctx := context.Background()

	// Consumer
	for i := 0; i < 10; i++ {
		go func() {
			for {
				if err := fullSem.Acquire(ctx, 1); err != nil {
					panic(err)
				}
				mux.Lock()
				firstItem := buffer[0]
				fmt.Println("Consumed:", firstItem)
				buffer = buffer[1:] // Consume an item
				mux.Unlock()
				emptySem.Release(1)
			}
		}()
	}

	// Producer
	for i := 0; i < 10; i++ {
		go func() {
			for {
				if err := emptySem.Acquire(ctx, 1); err != nil {
					panic(err)
				}
				mux.Lock()
				counter = (counter + 1) % BUF_SIZE

				buffer = append(buffer, byte(counter))
				// fmt.Println("Produced:", counter)
				mux.Unlock()
				fullSem.Release(1)
				time.Sleep(1000 * time.Millisecond)
			}
		}()
	}

	// Prevent main from exiting
	select {}
}
